girl_Names = ['Evelyn', 'Jessica', 'Somto', 'Edith', 'Liza', 'Madonna', 'Waje', 'Tola', 'Aisha','Latifa']
girl_Age =[17,16,17,18,16, 18,17,20,19,17]
girl_Height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
girl_Scores = [80,85,70,60,76,66,87,95,50,49]


boy_Names= ['Chinedu', 'Liam', 'Wale', 'Gbenga', 'Abiola', 'Kola', 'Kunie', 'George', 'Thomas' ,'Wesley']

boy_Age= [19,16,18,17,20,19,16,18,17,19]
boy_Height = [5.7,5.9,5.8,6.1,5.9,5.5,61,5.4,5.8,5.7]
boy_Scores = [74,87,75,68,66,78,87,98,54,60]
print("Names | Age | Height | scores")

for i in range(len(girl_Names)):
    print(girl_Names[i],'|',girl_Age[i],'|',girl_Height[i],'|',girl_Scores[i])

for i in range(len(boy_Names)):
    print(boy_Names[i],'|',boy_Age[i],'|',boy_Height[i],'|',boy_Scores[i])



