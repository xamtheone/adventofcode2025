def main [file] {
    open $file
    | lines
    | reduce --fold {pos: 50 s: 0} {|row, acc|
        mut newacc  = {pos: $acc.pos, s: $acc.s}
        let v = $row | str substring 1.. | into int
        if ($row | str substring 0..0) == 'R' {
            $newacc.pos += $v
        } else {
            $newacc.pos -= $v
        }
        if ($newacc.pos mod 100) == 0 {
            $newacc.s += 1
        }
        $newacc
    }
    | get s
}