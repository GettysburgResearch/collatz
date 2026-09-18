/** One cancellable job client shared by visible panels and agent commands. */
export class JobClient {
  constructor(onProgress = () => {}) {this.token = ''; this.jobs = new Map(); this.epochs = new Map(); this.onProgress = onProgress;}
  async api(path, options = {}) {
    const response = await fetch(path, {...options, headers: {'Content-Type': 'application/json', 'X-Observatory-Token': this.token, ...options.headers}});
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || `HTTP ${response.status}`);
    return data;
  }
  async init() {const health = await this.api('/api/health'); this.token = health.token; return health;}
  async run(request, channel = request.kind) {
    const epoch = (this.epochs.get(channel) || 0) + 1; this.epochs.set(channel, epoch);
    for (const [id, job] of this.jobs) if (job.channel === channel) await this.api(`/api/jobs/${id}`, {method:'DELETE'});
    // A cancelling worker still owns its slot. Wait, rather than overfilling it.
    for (let attempt = 0; this.jobs.size >= 2 && attempt < 400; attempt++) await new Promise(r => setTimeout(r, 30));
    if (this.epochs.get(channel) !== epoch) return null;
    let job;
    for (let attempt = 0; attempt < 100; attempt++) {
      try {job = await this.api('/api/jobs', {method:'POST', body:JSON.stringify(request)}); break;}
      catch (error) {if (!error.message.includes('Two jobs') || attempt === 99) throw error; await new Promise(r=>setTimeout(r,40));}
    }
    this.jobs.set(job.id, {channel, request}); this.onProgress(this.jobs);
    try {
      while (['running', 'cancelling'].includes(job.status)) {
        await new Promise(r => setTimeout(r, 55));
        job = await this.api(`/api/jobs/${job.id}`); this.onProgress(this.jobs, job);
      }
      if (this.epochs.get(channel) !== epoch) return null;
      if (!job.data || !['done','cancelled','timed_out'].includes(job.status)) throw new Error(job.error || `Job ${job.status}`);
      return job.data;
    } finally {this.jobs.delete(job.id); this.onProgress(this.jobs);}
  }
  async cancelAll() {await Promise.all([...this.jobs.keys()].map(id=>this.api(`/api/jobs/${id}`,{method:'DELETE'})));}
}
