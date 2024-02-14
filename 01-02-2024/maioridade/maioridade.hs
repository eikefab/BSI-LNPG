main :: IO() = do
    putStrLn "Insira sua idade: "
    input <- getLine

    let age = read input :: Int

    if age >= 18
        then putStrLn "Você é maior de idade."
        else putStrLn "Você é menor de idade."