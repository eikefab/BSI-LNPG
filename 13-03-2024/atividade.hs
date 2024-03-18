import Data.List (delete)

adicionar agenda = do
    putStrLn "Nome do evento: "
    evento <- getLine

    return $ agenda ++ [evento]

retirar agenda = do
    putStrLn "Indice do evento a ser removido: "
    indice <- getLine

    let agendaNova = delete (agenda !! read indice) agenda

    return agendaNova

item agenda indice
    | length agenda == indice = putStrLn ""
    | otherwise = do
        putStrLn $ agenda !! indice

        item agenda (indice + 1)

ver agenda = do
    putStrLn "Itens em sua agenda:\n"

    item agenda 0

controle opcao agenda
    | opcao == "1" = do
        agendaAtualizada <- adicionar agenda
        novaOpcao <- menu

        controle novaOpcao agendaAtualizada
    | opcao == "2" = do
        agendaAtualizada <- retirar agenda
        novaOpcao <- menu

        controle novaOpcao agendaAtualizada
    | opcao == "3" = do
        ver agenda
        novaOpcao <- menu

        controle novaOpcao agenda
    | otherwise = putStrLn "Programa finalizado."
        
menu = do
    putStrLn "\nSelecione uma opção:"
    putStrLn "1. Adicionar evento"
    putStrLn "2. Remover evento"
    putStrLn "3. Visualizar agenda"
    putStrLn "4. Sair"

    getLine

main :: IO ()
main = do
    opcaoInicial <- menu

    controle opcaoInicial []