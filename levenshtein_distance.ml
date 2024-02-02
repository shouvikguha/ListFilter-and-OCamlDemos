let levenshtein s t =
  let m = String.length s and n = String.length t in
  let d = Array.make_matrix (m+1) (n+1) 0 in
  for i = 0 to m do d.(i).(0) <- i done;
  for j = 0 to n do d.(0).(j) <- j done;
  for j = 1 to n do
    for i = 1 to m do
      let substitution_cost = if s.[i-1] = t.[j-1] then 0 else 1 in
      d.(i).(j) <- min (min
        (d.(i-1).(j) + 1)    (* deletion *)
        (d.(i).(j-1) + 1))   (* insertion *)
        (d.(i-1).(j-1) + substitution_cost) (* substitution *)
    done
  done;
  d.(m).(n)
;;

(* Test case *)
let () =
  let dist = levenshtein "kitten" "sitting" in
  Printf.printf "Levenshtein distance: %d\n" dist
