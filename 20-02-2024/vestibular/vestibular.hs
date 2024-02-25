import Text.Printf (printf)
findAnswers = map (read :: String -> Int) . words <$> getLine

fetch arr = do
    name <- getLine

    if name == "*"
        then arr
        else do
            answers <- findAnswers

            let sum = do
                    previous <- arr

                    return $ previous ++ [(name, answers)]

            fetch sum

match template answers =
    let tuples = zip template answers
    in sum $ map (\(x, y) -> if x == y then 1 else 0) tuples

peak results index top student
    | length results == index = student
    | otherwise =
        let target = results !! index
            (name, score) = target

        in if score > top
            then peak results (index + 1) score target
            else peak results (index + 1) top student

bottom results index bot student
    | length results == index = student
    | otherwise =
        let target = results !! index
            (name, score) = target

        in if bot > score
            then bottom results (index + 1) score target
            else bottom results (index + 1) bot student

mid results answers =
    let students = length $ filter (\(x, score) -> score > div (length answers) 2) results
        amount = fromIntegral $ length results
    
    in (fromIntegral students / amount * 100)

main :: IO () = do
    answers <- findAnswers
    students <- fetch $ return []

    let results = map (\(x, y) -> (x, match answers y)) students
        top = peak results 0 0 ("", 0)
        (topName, topScore) = top
        bot = bottom results 0 topScore top
        (botName, botScore) = bot

    putStrLn $ topName ++ ": " ++ show topScore
    putStrLn $ botName ++ ": " ++ show botScore

    let midAmount = mid results answers :: Double

    printf "%.2f%%" midAmount
    putStrLn " acertaram mais que a metade."
