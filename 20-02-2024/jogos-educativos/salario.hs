import Text.Printf (printf)

total price sold = price * fromIntegral sold

calcBonus total agg times index
    | times == index = agg
    | otherwise = calcBonus (total * 0.92) (agg + (total * 0.08)) times (index + 1)

bonus total 15 = total * 0.08
bonus total sold = do
    let times = div sold 15

    calcBonus total 0 times 0

wage total bonus = (total / 2) + bonus

main :: IO () = do
    let price = 19.9

    putStrLn "Informe a quantidade de vendas: "

    sold <- readLn :: IO Int

    let revenue = total price sold :: Float
    let empBonus = bonus revenue sold :: Float
    let empWage = wage revenue empBonus :: Float

    printf "%.2f\n" revenue
    printf "%.2f\n" empBonus
    printf "%.2f\n" empWage