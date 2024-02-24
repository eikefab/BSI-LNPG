import Control.Monad (when)
import Distribution.Compat.Prelude (exitSuccess)

getInput input = do
    putStrLn input
    getLine

pax n = do
    putStrLn ""
    putStrLn ("Passageiro (" ++ show n ++ ")")

    rg <- getInput "RG (ou 'Nao possui'):"

    when (rg == "Nao possui") $ do 
        putStrLn "A saída é nessa direção."
        exitSuccess

    birthdate <- getInput "Data de nascimento (RG):"

    ticket <- getInput "Passagem (ou 'Nao possui'):"

    when (ticket == "Nao possui") $ do
        putStrLn "A recepção é nessa direção."
        exitSuccess

    ticketBirthdate <- getInput "Data de nascimento (Passagem):"

    when (birthdate /= ticketBirthdate) $ do
        putStrLn "190"
        exitSuccess
    
    ticketSeat <- getInput "Assento (ex.: A12):"

    putStrLn ("O seu assento é " ++ ticketSeat ++ ", tenha um ótimo dia.")
    putStrLn ""

passengers current total
    | current == total = pure ()
    | otherwise = do
        pax (current + 1)
        passengers (current + 1) total

main :: IO () = do
    i <- getInput "Informe o número de passageiros: "

    let total = read i :: Int

    passengers 0 total