import ReturnAtlas

/-! A complete positive descent with charged cofactors 1 modulo 16 and at
most 24 times the original input. F and B are full ordinary positive
odd blocks, or a truncated last forward block ending at an even integer. -/
set_option autoImplicit false
set_option warningAsError true
namespace ReturnTwentyFour
open ReturnAtlas
open EarlierOffsets (Good)
private abbrev F := Move.forward
private abbrev B := Move.backward
private abbrev C := Move.charge

def certificate : Tree :=
(.two
  (.three
    (.two
      (.two
        (.leaf [F 1,F 3])
        (.two
          (.leaf [F 1,B 3,B 2,C,F 1,F 3,F 5])
          (.leaf [F 1,F 2,F 2])))
      (.two
        (.leaf [F 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,B 1])
        (.leaf [F 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 8])))
    (.three
      (.two
        (.two
          (.two
            (.three
              (.two
                (.two
                  (.leaf [F 1,F 1,F 2,F 3])
                  (.two
                    (.leaf [F 1,F 1,F 2,F 2,F 2])
                    (.leaf [F 1,F 1,C,F 1,F 5])))
                (.two
                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 9])
                  (.two
                    (.leaf [F 1,F 1,F 2,F 1,F 3])
                    (.three
                      (.three
                        (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 3,B 1,B 4,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1,B 1])
                        (.three
                          (.three
                            (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 1,B 1,B 1,B 1])
                            (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 3,B 1,B 4,B 1,B 2,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1,B 1])
                            (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,B 3,B 2,C,F 1,F 3,F 4,B 2,B 2,C,F 1,F 4,B 2,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7]))
                          (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,B 2,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1])
                          (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,F 1,F 1,F 1,F 5]))
                        (.leaf [F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 2,B 2,C,F 1,F 5,F 5]))
                      (.three
                        (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 1,F 5])
                        (.three
                          (.leaf [B 4,B 2,B 2,B 1,B 3,B 2,C,F 1,F 3,F 2,F 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 3,B 1,B 4,B 1,B 2,B 1,B 1,B 2,B 2,C,F 1,F 5,F 3,F 1,F 2,F 3])
                          (.three
                            (.three
                              (.leaf [B 4,B 2,B 2,B 1,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 6])
                              (.two
                                (.two
                                  (.leaf [F 1,F 1,F 2,F 1,F 2,F 3])
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 5,B 1]))
                                (.two
                                  (.two
                                    (.two
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3,B 1])
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 4]))
                                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 5,B 3,B 2,B 2,C,F 1,F 4,B 2,B 2,C,F 1,F 7,B 1,B 1]))
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,F 3])))
                              (.three
                                (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,B 3,B 2,C,F 1,F 3,F 4,B 2,B 2,C,F 1,F 4,B 2,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 3,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 4,B 2,C,F 1,F 5])
                                (.leaf [B 4,B 2,B 2,B 1,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7])
                                (.two
                                  (.two
                                    (.two
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 5,B 3,B 2,B 2,C,F 1,F 4,B 2,B 2,C,F 1,F 7,B 1,B 1])
                                      (.two
                                        (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 4])
                                        (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3,B 1])))
                                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,F 3]))
                                  (.two
                                    (.leaf [F 1,F 1,F 2,F 1,F 2,F 3])
                                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 5,B 1])))))
                            (.three
                              (.two
                                (.two
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 5,B 1])
                                  (.leaf [F 1,F 1,F 2,F 1,F 2,F 3]))
                                (.two
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,F 3])
                                  (.two
                                    (.two
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3,B 1])
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 4]))
                                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 5,B 3,B 2,B 2,C,F 1,F 4,B 2,B 2,C,F 1,F 7,B 1,B 1]))))
                              (.two
                                (.two
                                  (.two
                                    (.two
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 4])
                                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3,B 1]))
                                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 5,B 3,B 2,B 2,C,F 1,F 4,B 2,B 2,C,F 1,F 7,B 1,B 1]))
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,F 3]))
                                (.two
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 5,B 1])
                                  (.leaf [F 1,F 1,F 2,F 1,F 2,F 3])))
                              (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,B 3,B 2,C,F 1,F 3,F 4,B 2,B 2,C,F 1,F 4,B 2,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 3,B 2,B 1,B 1,B 2,B 2,C,F 1,F 5,F 4,B 2,C,F 1,F 5]))
                            (.leaf [B 4,B 2,B 2,B 1,B 1,B 2,B 2,C,F 1,F 5,F 6]))
                          (.two
                            (.two
                              (.leaf [F 1,F 1,F 2,F 1,F 2,F 3])
                              (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 5,B 1]))
                            (.two
                              (.two
                                (.two
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3,B 1])
                                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,F 2,F 4,F 4]))
                                (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 5,B 3,B 2,B 2,C,F 1,F 4,B 2,B 2,C,F 1,F 7,B 1,B 1]))
                              (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,F 3]))))
                        (.three
                          (.leaf [B 4,B 2,B 2,B 1,B 2,B 2,C,F 1,F 10])
                          (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 1,F 5])
                          (.three
                            (.three
                              (.leaf [B 4,B 2,B 2,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1])
                              (.three
                                (.leaf [F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 1,B 1,B 1,B 1])
                                (.leaf [F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 4,B 1,B 1,B 1,B 1,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 2,F 1,F 2,F 3,F 1,F 2,F 1,F 7])
                                (.leaf [F 1,B 3,B 1,B 4,B 1,B 2,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1]))
                              (.leaf [F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,B 1,B 1]))
                            (.leaf [F 1,B 3,B 1,B 4,B 1,B 2,B 1,B 2,B 2,C,F 1,F 7,B 1,B 1])
                            (.leaf [F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 2,F 3,F 1,F 2,F 1,F 7]))))
                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,F 1,F 3,B 1,B 2,B 1,B 4,B 2,B 2,B 1,B 2,B 2,C,F 1,F 10])))))
              (.three
                (.two
                  (.two
                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 8,B 2,B 1,B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,B 3,B 2,C,F 1,F 3,F 4,B 2,B 2,C,F 1,F 4,B 2,B 2,B 2,B 1,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 1,F 7])
                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 9]))
                  (.two
                    (.two
                      (.leaf [F 1,F 1,C,F 1,F 5])
                      (.leaf [F 1,F 1,F 2,F 2,F 2]))
                    (.leaf [F 1,F 1,F 2,F 3])))
                (.three
                  (.leaf [F 1,B 3,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 1,F 9])
                  (.three
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,F 3])
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 1])
                    (.three
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 1])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 4,B 2,C,F 1,F 3,F 1,F 3,F 3,F 2,F 3])))
                  (.leaf [B 4,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 2,B 2,C,F 1,F 9]))
                (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 5,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 5]))
              (.leaf [F 1,B 3,B 1,B 4,B 2,C,F 1,F 3,F 1,F 9]))
            (.leaf [F 1,F 1,F 3]))
          (.two
            (.three
              (.three
                (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 6,B 4,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 5])
                (.two
                  (.two
                    (.two
                      (.leaf [F 1,F 1,F 1,F 2,F 3])
                      (.two
                        (.two
                          (.leaf [F 1,F 1,F 1,C,F 1,F 6])
                          (.leaf [F 1,F 1,F 1,C,F 1,F 5,B 1]))
                        (.two
                          (.two
                            (.two
                              (.leaf [F 1,F 1,F 1,F 2,C,F 1,F 5,B 1])
                              (.leaf [F 1,F 1,F 1,F 2,C,F 1,F 6]))
                            (.two
                              (.two
                                (.leaf [F 1,F 1,F 1,F 2,F 2,F 2,F 2,F 2])
                                (.leaf [F 1,F 1,F 1,F 2,F 2,C,F 1,F 5]))
                              (.leaf [F 1,F 1,F 1,F 2,F 2,F 2,F 3])))
                          (.leaf [F 1,F 1,F 1,F 2,F 2,F 3]))))
                    (.two
                      (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,F 3,F 3])
                      (.leaf [F 1,F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 6])))
                  (.two
                    (.leaf [F 1,F 1,F 1,F 3,B 1])
                    (.leaf [F 1,F 1,F 1,F 4])))
                (.three
                  (.three
                    (.three
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 1])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 4,B 2,C,F 1,F 3,F 1,F 3,F 3,F 2,F 3]))
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,F 3])
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 1]))
                  (.leaf [B 4,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 2,B 2,C,F 1,F 9])
                  (.leaf [F 1,B 3,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 1,F 7,F 2])))
              (.leaf [F 1,B 3,B 1,B 4,B 2,C,F 1,F 3,F 1,F 7,F 2])
              (.two
                (.two
                  (.leaf [F 1,F 1,F 1,F 4])
                  (.leaf [F 1,F 1,F 1,F 3,B 1]))
                (.two
                  (.two
                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,F 3,F 3])
                    (.leaf [F 1,F 1,F 1,F 2,F 1,B 3,B 1,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 6]))
                  (.two
                    (.leaf [F 1,F 1,F 1,F 2,F 3])
                    (.two
                      (.two
                        (.leaf [F 1,F 1,F 1,C,F 1,F 5,B 1])
                        (.leaf [F 1,F 1,F 1,C,F 1,F 6]))
                      (.two
                        (.two
                          (.two
                            (.leaf [F 1,F 1,F 1,F 2,C,F 1,F 6])
                            (.leaf [F 1,F 1,F 1,F 2,C,F 1,F 5,B 1]))
                          (.two
                            (.two
                              (.leaf [F 1,F 1,F 1,F 2,F 2,F 2,F 2,F 2])
                              (.leaf [F 1,F 1,F 1,F 2,F 2,C,F 1,F 5]))
                            (.leaf [F 1,F 1,F 1,F 2,F 2,F 2,F 3])))
                        (.leaf [F 1,F 1,F 1,F 2,F 2,F 3])))))))
            (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 3,B 1,B 2,B 3,B 2,C,F 1,F 3,F 7])))
        (.two
          (.two
            (.leaf [F 1,F 2,F 2])
            (.three
              (.three
                (.three
                  (.leaf [F 1,B 3,B 3,B 1,B 1,B 3,B 2,C,F 1,F 3,F 2,F 1,F 1,F 6,F 3])
                  (.three
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 1])
                    (.three
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 1])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5])
                      (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 1,B 4,B 2,C,F 1,F 3,F 1,F 3,F 3,F 2,F 5]))
                    (.leaf [F 1,B 3,B 1,B 2,B 1,B 1,B 3,B 2,C,F 1,F 3,B 1,B 2,B 2,C,F 1,F 7,F 3]))
                  (.leaf [B 4,B 2,C,F 1,F 3,B 1,B 2,B 2,B 1,B 2,B 2,C,F 1,F 9]))
                (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,B 3,B 2,C,F 1,F 3,F 4,B 2,B 2,C,F 1,F 4,B 2,B 2,B 2,B 1,B 1,B 1,B 2,B 2,C,F 1,F 5,F 1,F 7])
                (.two
                  (.two
                    (.two
                      (.leaf [F 1,F 2,F 1,F 2,F 2])
                      (.leaf [F 1,F 2,F 1,B 3,B 1,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3]))
                    (.leaf [F 1,F 2,F 1,F 3]))
                  (.two
                    (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 7])
                    (.leaf [F 1,F 2,F 1,B 3,B 1,B 3,B 2,C,F 1,F 3,F 2,F 6]))))
              (.leaf [F 1,B 3,B 1,B 4,B 2,C,F 1,F 3,F 1,F 6,F 3])
              (.two
                (.two
                  (.two
                    (.leaf [F 1,F 2,F 1,B 3,B 1,B 3,B 2,C,F 1,F 3,F 2,F 4,F 3])
                    (.leaf [F 1,F 2,F 1,F 2,F 2]))
                  (.leaf [F 1,F 2,F 1,F 3]))
                (.two
                  (.leaf [F 1,F 2,F 1,B 3,B 1,B 3,B 2,C,F 1,F 3,F 2,F 6])
                  (.leaf [B 4,B 2,C,F 1,F 3,F 1,F 4,B 2,B 2,C,F 1,F 7])))))
          (.leaf [F 1,F 3])))
      (.leaf [B 2,B 2,C,F 1,F 5])
      (.leaf [B 2,B 1]))
    (.leaf [B 1]))
  (.leaf [F 2]))

set_option maxRecDepth 30000 in
set_option maxHeartbeats 0 in
theorem checked : check 24 certificate ⟨2,3⟩=true := by decide +kernel

theorem binary_defect (n : ℕ) (positive : 0<n) (bad : ¬Good n) :
    ∃ w, 0<w ∧ w%16=1 ∧ w≤24*n ∧ ¬Good w ∧ Good (3*w) :=
  bounded_return 24 certificate checked n positive bad

#print axioms checked
#print axioms binary_defect
end ReturnTwentyFour
