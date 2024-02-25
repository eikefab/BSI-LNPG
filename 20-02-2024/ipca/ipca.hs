import Text.Printf (printf)

fetch arr = do
    input <- getLine

    let extract = words input
        sum = do
            previous <- arr

            return $ previous ++ [extract]

    if input == "*"
        then arr
        else fetch sum

peak ipca current highest item
    | length ipca == current = item
    | otherwise =
        let target = ipca !! current
            value = read $ head target :: Float

        in if value > highest
            then peak ipca (current + 1) value target
            else peak ipca (current + 1) highest item

bottom ipca current lowest item
    | length ipca == current = item
    | otherwise =
        let target = ipca !! current
            value = read $ head target :: Float

        in if lowest > value
            then bottom ipca (current + 1) value target
            else bottom ipca (current + 1) lowest item

total ipca current agg
    | length ipca == current = agg
    | otherwise = do
        let item = ipca !! current
            value = read $ head item :: Float

        total ipca (current + 1) (agg + value)

avg ipca = total ipca 0 0.0 / fromIntegral (length ipca)

date item = do
    let a = read (item !! 1) :: Int
    let b = read (item !! 2) :: Int

    if a > b
        then [b, a]
        else [a, b]

main :: IO () = do
    ipca <- fetch $ return []

    putStrLn ""

    let peakIpca = peak ipca 0 0 []

    let peakIpcaValue = read $ head peakIpca :: Float
    let peakIpcaDate = date peakIpca

    let peakIpcaMonth = head peakIpcaDate
    let peakIpcaYear = last peakIpcaDate

    printf "%.2f" peakIpcaValue
    putStrLn ("% " ++ show peakIpcaMonth ++ "/" ++ show peakIpcaYear)

    let bottomIpca = bottom ipca 0 peakIpcaValue peakIpca

    let bottomIpcaValue = read $ head bottomIpca :: Float
    let bottomIpcaDate = date bottomIpca

    let bottomIpcaMonth = head bottomIpcaDate
    let bottomIpcaYear = last bottomIpcaDate

    printf "%.2f" bottomIpcaValue
    putStrLn ("% " ++ show bottomIpcaMonth ++ "/" ++ show bottomIpcaYear)
    
    let avgIpca = avg ipca

    printf "%.2f" avgIpca
    putStrLn "%"