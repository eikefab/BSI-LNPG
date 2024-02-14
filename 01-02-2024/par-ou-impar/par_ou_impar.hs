main :: IO () = do
    putStrLn "Informe um inteiro: "
    input <- getLine

    let a = read input :: Int

    if even a 
        then putStrLn (show a ++ " é par.")
        else putStrLn (show a ++ " é ímpar.")
