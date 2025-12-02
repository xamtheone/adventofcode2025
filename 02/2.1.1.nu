def main [file] {
    open $file
    | split row ','
    | reduce --fold 0 {|range, acc|
        let parts = $range | split row '-' | each {|| into int }
        ($parts.0..$parts.1 | reduce --fold 0 {|i, acc2|
            if ($i | into string) =~ '^(.+)\1$' {
                $acc2 + $i
            } else {
                $acc2
            }
        }) + $acc
    }
}