import Text.Printf (printf)

calc length index agg
    | length == index = agg
    | otherwise =
        let seq = 1 / (fromIntegral value ^ 3)
        in if index == 0
                then calc length (index + 1) seq
                else if even index
                    then calc length (index + 1) (agg + seq)
                    else calc length (index + 1) (agg - seq)
    where value = (index * 2) + 1

calcPi n = (calc n 0 0 * 32) ** (1 / 3)

main :: IO () = do
    putStrLn "Informe o número de termos: "
    n <- readLn :: IO Int

    let val = calcPi n :: Float

    printf "%.5f\n" val