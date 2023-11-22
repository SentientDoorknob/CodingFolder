m_data = read.table("C:\\Users\\justa\\Downloads\\py_output.txt")
key_length <- 11

head(m_data)
m_scores = matrix(round(m_data$V3, 2), byrow = TRUE, ncol = key_length)
row.names(m_scores) = m_data$V2[1:key_length]
colnames(m_scores) = m_data$V2[1:key_length]
View(m_scores)
