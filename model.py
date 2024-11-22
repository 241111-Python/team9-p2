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
        self.RowNumber = RowNumber
        self.CustomerId = CustomerId
        self.Surname = Surname
        self.CreditScore = CreditScore
        self.Geography = Geography
        self.Gender = Gender
        self.Age = Age
        self.Tenure = Tenure
        self.Balance = Balance
        self.NumOfProducts = NumOfProducts
        self.HasCrCard = HasCrCard
        self.IsActiveMember = IsActiveMember
        self.EstimatedSalary = EstimatedSalary
        self.Exited = Exited
        self.Complain = Complain
        self.Satisfaction_Score = Satisfaction_Score
        self.Card_Type = Card_Type
        self.Point_Earned = Point_Earned

    def __str__(self):
        return f"{self.RowNumber}: {self.Surname} - {self.CreditScore}"
