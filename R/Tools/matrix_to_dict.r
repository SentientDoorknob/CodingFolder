m_data <- read.csv("C:\\Users\\justa\\Downloads\\things.csv")
dim(m_data)
scores <- as.vector(t(as.matrix(m_data)))
pairs = expand.grid(LETTERS,LETTERS)
pairs_2_the_grand_opening_plus_plus_the_ultra_omega_experience = paste0(pairs$Var2,pairs$Var1) 


data_output = data.frame(digram=pairs_2_the_grand_opening_plus_plus_the_ultra_omega_experience, 
                         scores = scores)

write.table(data_output,"C:\\Users\\justa\\Downloads\\output.txt", quote=TRUE, row.names=FALSE)
