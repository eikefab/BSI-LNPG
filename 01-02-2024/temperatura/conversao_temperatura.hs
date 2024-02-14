fahrenheit a = (fromIntegral a * 1.8) + 32

main :: IO () = do
    putStrLn "Informe a temperatura em ºC: "
    input <- getLine

    let celsius = read input :: Int

    putStrLn (show celsius ++ "ºC equivalem a " ++ show (fahrenheit celsius) ++ "ºF")