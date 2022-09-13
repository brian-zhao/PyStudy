def canConstruct(ransomNote: str, magazine: str) -> bool:
    for i in ransomNote:
        if i in magazine:
            magazine = magazine.replace(i, "", 1)
        else:
            return False
    return True


if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"
    assert canConstruct(ransomNote, magazine) is False

    ransomNote = "aa"
    magazine = "ab"
    assert canConstruct(ransomNote, magazine) is False

    ransomNote = "aa"
    magazine = "aab"
    assert canConstruct(ransomNote, magazine) is True
