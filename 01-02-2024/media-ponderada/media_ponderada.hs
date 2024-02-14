import Data.Array (listArray, elems)

main :: IO () = do
  putStrLn "Digite as 3 notas:"
  inputs <- sequence [getLine, getLine, getLine]

  let notas = listArray(1, 3) (map read inputs :: [Float])

  putStrLn "Digite os 3 pesos:"
  inputs <- sequence [getLine, getLine, getLine]

  let pesos = listArray(1, 3) (map read inputs :: [Float]) -- Pra usar no zipWith, ambas as listas devem ter o mesmo tipo de elementos
      pesoTotal = sum (elems pesos)
      valoresNotas = zipWith (*) (elems notas) (elems pesos)
    
  let media = sum valoresNotas  / pesoTotal

  putStrLn ("Média final: " ++ show media)