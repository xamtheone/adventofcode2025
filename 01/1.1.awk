BEGIN { pos = 50 }
{
    d = substr($0, 1, 1)
    v = substr($0, 2)
    pos += d == "R" ? v : -v
    if (pos % 100 == 0) s += 1
}
END { print s }