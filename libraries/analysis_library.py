import json
from model.analysis import Analysis
from libraries.library import csvRead

def printAnalysisEntries(entry_list):
    while True:
        print("\nEnter A: Average credit score by country")
        print("Enter B: Average balance based on age")
        print("Enter C: Average credit score based on tenure")
        print("Enter D: Estimated salary based on gender")
        print("Enter E: Export Analysis")
        print("Enter X: Exit")
        user_input = input("Enter Here: ")
        if user_input.upper() == "A":
            regions, countryScoreAvgs = geoScoreAvg(entry_list)
            for index in range(len(regions)):
                print(
                    f"The average credit score of {regions[index]} is {countryScoreAvgs[index]:.2f}"
                )

        elif user_input.upper() == "B":
            ages, balanceAvgs = balanceAgeAvg(entry_list)
            for index in range(len(ages)):
                print(
                    f"The average account balance for ages {ages[index]} is ${balanceAvgs[index]:.2f}"
                )

        elif user_input.upper() == "C":
            tenures, creditScoreAvgs = tenureScoreAvg(entry_list)
            for index in range(len(tenures)):
                print(
                    f"The average credit score of tenure rating {tenures[index]} is {creditScoreAvgs[index]:.2f}"
                )

        elif user_input.upper() == "D":
            genders, salaryGenderAvgs = salaryGenderAvg(entry_list)
            for index in range(len(genders)):
                print(
                    f"The overall estimated salary for {genders[index]} is about ${salaryGenderAvgs[index]:.2f}"
                )

        elif user_input.upper() == "E":
            exportAnalysis(entry_list)
        elif user_input.upper() == "X":
            break
        else:
            print("Invalid input!. Please review the options and try again")


def geoScoreAvg(entry_list):
    regions = []
    countryScoreAvgs = []
    for entry in entry_list:
        if entry.Geography not in regions:
            regions.append(entry.Geography)
    for country in regions:
        creditSum = 0
        countryEntries = 0
        countryScoreAvg = 0
        for entry in entry_list:
            if country == entry.Geography:
                creditSum = creditSum + entry.CreditScore
                countryEntries = countryEntries + 1
        countryScoreAvg = creditSum / countryEntries
        countryScoreAvgs.append(countryScoreAvg)

    return (regions, countryScoreAvgs)


def balanceAgeAvg(entry_list):
    ages = ["18-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+"]
    balances = [0] * len(ages)
    entries = [0] * len(ages)
    balanceAverages = [0] * len(ages)
    for entry in entry_list:
        if entry.Age >= 18 and entry.Age <= 29:
            balances[0] = balances[0] + entry.Balance
            entries[0] = entries[0] + 1
        if entry.Age >= 30 and entry.Age <= 39:
            balances[1] = balances[1] + entry.Balance
            entries[1] = entries[1] + 1
        if entry.Age >= 40 and entry.Age <= 49:
            balances[2] = balances[2] + entry.Balance
            entries[2] = entries[2] + 1
        if entry.Age >= 50 and entry.Age <= 59:
            balances[3] = balances[3] + entry.Balance
            entries[3] = entries[3] + 1
        if entry.Age >= 60 and entry.Age <= 69:
            balances[4] = balances[4] + entry.Balance
            entries[4] = entries[4] + 1
        if entry.Age >= 70 and entry.Age <= 79:
            balances[5] = balances[5] + entry.Balance
            entries[5] = entries[5] + 1
        if entry.Age >= 80 and entry.Age <= 89:
            balances[6] = balances[6] + entry.Balance
            entries[6] = entries[6] + 1
        if entry.Age >= 90:
            balances[7] = balances[7] + entry.Balance
            entries[7] = entries[7] + 1
    for i in range(len(ages)):
        if entries[i] != 0:
            balanceAverages[i] = balances[i] / entries[i]
        else:
            balanceAverages[i] = 0

    return (ages, balanceAverages)


def tenureScoreAvg(entry_list):
    tenures = []
    creditScoreAvgs = []
    for entry in entry_list:
        if entry.Tenure not in tenures:
            tenures.append(entry.Tenure)
    tenures.sort()
    for tenure in tenures:
        creditSum = 0
        tenureEntries = 0
        tenureScoreAvg = 0
        for entry in entry_list:
            if tenure == entry.Tenure:
                creditSum = creditSum + entry.CreditScore
                tenureEntries = tenureEntries + 1
        tenureScoreAvg = creditSum / tenureEntries
        creditScoreAvgs.append(tenureScoreAvg)

    return (tenures, creditScoreAvgs)


def salaryGenderAvg(entry_list):
    genders = ["Male", "Female"]
    estimatedSalaries = [0] * len(genders)
    entries = [0] * len(genders)
    salaryAverages = [0] * len(genders)
    for entry in entry_list:
        if entry.Gender == genders[0]:
            estimatedSalaries[0] = estimatedSalaries[0] + entry.EstimatedSalary
            entries[0] = entries[0] + 1
        else:
            estimatedSalaries[1] = estimatedSalaries[1] + entry.EstimatedSalary
            entries[1] = entries[1] + 1
    for i in range(len(genders)):
        if entries[i] != 0:
            salaryAverages[i] = estimatedSalaries[i] / entries[i]
    return (genders, salaryAverages)


def exportAnalysis(entry_list):
    # gets a tuple for average credit score of regions: regions, score
    avg_geo_score = geoScoreAvg(entry_list)

    # gets a tuple for avergare salary of genders: genders, salary
    avg_salary_gender = salaryGenderAvg(entry_list)

    # gets a tuple for average credit score of tenure(time in the bank): tenures, score
    avg_score_tenure = tenureScoreAvg(entry_list)

    # gets a tuple for average balance of age: ages, balances
    avg_balance_age = balanceAgeAvg(entry_list)

    # Creates an analysis object and uses add_entry method to save each entry with their respective key on the
    # data object
    analysis_obj = Analysis()
    analysis_obj.add_entry(
        key="AverageGeographyBased", keys=avg_geo_score[0], values=avg_geo_score[1]
    )
    analysis_obj.add_entry(
        key="SalaryGenderBased", keys=avg_salary_gender[0], values=avg_salary_gender[1]
    )
    analysis_obj.add_entry(
        key="AverageCreditScoreTenureBased",
        keys=avg_score_tenure[0],
        values=avg_score_tenure[1],
    )
    analysis_obj.add_entry(
        key="AverageBalanceAgeBased", keys=avg_balance_age[0], values=avg_balance_age[1]
    )

    try:
        with open("./data/analysis_output.json", "w") as jsonFile:
            jsonFile.write(json.dumps(analysis_obj.data, indent=4))
            jsonFile.close()
    except Exception as e:
        print(e)

def ratioNumProdByPointsAvg(entry_list):
    pointsEarnedData= dict()
    for entry in entry_list:
        if entry.Point_Earned not in pointsEarnedData:
            pointsEarnedData[entry.Point_Earned] = {"customer_count":0, "num_of_products":0}
        pointsEarnedData[entry.Point_Earned]["customer_count"] += 1
        pointsEarnedData[entry.Point_Earned]["num_of_products"] += entry.NumOfProducts
    
    ratio = dict()
    for pointsEarned, data in pointsEarnedData.items():
        ratio[pointsEarned] = data["num_of_products"] / data["customer_count"]

    return dict(sorted(ratio.items()))
    


def crontabAnalysis(path):
    entry_list = csvRead(path)

    return ratioNumProdByPointsAvg(entry_list)
