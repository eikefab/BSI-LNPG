main :: IO ()

main = do
    putStrLn "Informe o primeiro inteiro: "
    input <- getLine
    let a = read input :: Int

    putStrLn "Informe o segundo inteiro: "
    input <- getLine
    let b = read input :: Int

    putStrLn ""
    putStrLn (show a ++ " + " ++ show b ++ " = " ++ show (a + b))
    putStrLn (show a ++ " - " ++ show b ++ " = " ++ show (a - b))
    putStrLn (show a ++ " * " ++ show b ++ " = " ++ show (a * b))
    putStrLn (show a ++ " / " ++ show b ++ " = " ++ show (fromIntegral a / fromIntegral b)) -- Por algum motivo, o Haskell pede que ambos sejam valores fracionários...
    putStrLn ""