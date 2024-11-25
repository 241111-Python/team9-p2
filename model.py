class Data:
    def __init__(
        self,
        RowNumber,
        CustomerId,
        Surname,
        CreditScore,
        Geography,
        Gender,
        Age,
        Tenure,
        Balance,
        NumOfProducts,
        HasCrCard,
        IsActiveMember,
        EstimatedSalary,
        Exited,
        Complain,
        Satisfaction_Score,
        Card_Type,
        Point_Earned,
    ):
        self.RowNumber = int(RowNumber)
        self.CustomerId = int(CustomerId)
        self.Surname = Surname
        self.CreditScore = int(CreditScore)
        self.Geography = Geography
        self.Gender = Gender
        self.Age = int(Age)
        self.Tenure = Tenure
        self.Balance = float(Balance)
        self.NumOfProducts = int(NumOfProducts)
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = float(EstimatedSalary)
        self.Exited = Exited
        self.Complain = Complain
        self.Satisfaction_Score = Satisfaction_Score
        self.Card_Type = Card_Type
        self.Point_Earned = int(Point_Earned)

    def __str__(self):
        return f"{self.CustomerId}: {self.Surname} - {self.Tenure} - {self.CreditScore} - {self.Point_Earned} - {self.Balance}"
