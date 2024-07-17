is_anagram <- function(str1, str2) {
  return(sort(unlist(strsplit(tolower(str1), ""))) == sort(unlist(strsplit(tolower(str2), ""))))
}

print(is_anagram("listen", "silent"))

