"""Integer strip count for 512 consecutive odd inputs on a bounded excursion."""
import json


def count_block(length, start):
    scale, rise, width = 100000, 58496, 244000
    counts = {0: 1}
    for time in range(1, length+1):
        height = start + time*rise
        low = (height-width+scale-1)//scale
        high = height//scale
        counts = {d: counts.get(d, 0)+counts.get(d-1, 0) for d in range(low, high+1)}
    return sum(counts.values())


def require(test, explanation):
    if not test:
        raise ArithmeticError(explanation)


def main():
    length = 512
    require(2**158496 < 3**100000 < 2**158497, 'log2(3/2) enclosure')
    require(267**100 < 50**100 * 2**242, 'physical width')
    total = sum(count_block(length, 1000*i) for i in range(245))
    require(total**100 < 3**(49*length), 'strictly sub-square-root word bound')
    print(json.dumps({'block_length':length, 'starting_bins':245, 'word_count_upper':total,
                      'strict_check':'C^100 < 3^(49*512)'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
