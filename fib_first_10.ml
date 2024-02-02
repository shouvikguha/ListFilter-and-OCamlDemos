let rec fib n = 
  match n with
  | 0 -> 0
  | 1 -> 1
  | _ -> fib (n - 1) + fib (n - 2)

let () =
  let rec print_fib i max =
    if i <= max then
      begin
        Printf.printf "%d " (fib i);
        print_fib (i + 1) max
      end
  in
  print_string "First 10 Fibonacci numbers: ";
  print_fib 0 9;
  print_newline ()
