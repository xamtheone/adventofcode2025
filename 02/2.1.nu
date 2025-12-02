def main [file] {
    open $file
    | split row ','
    | reduce --fold 0 {|range, acc|
        let parts = $range | split row '-' | each {|| into int }
        mut s = 0
        for i in $parts.0..$parts.1 {
            if ($i | into string) =~ '^(.+)\1$' {
                $s += $i
            }
        }
        $s + $acc
    }
}