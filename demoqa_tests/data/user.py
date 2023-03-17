def get_user():
    alexsanda = User(
        firstName='Alexsandra',
        lastName='Kr',
        userEmail='test@test.com',
        userNumber='8922121245',
        address='Tyumen, Moskovskaya Street 42',
        radio_button_type='gender',
        gender_value='Female',
        date_type='dateOfBirthInput',
        month='December',
        year='1997',
        day='11',
        input_subject='computer',
        select_subject='Computer Science',
        checkbox_type='hobbies',
        checkbox_value='Sports',
        picture_name='foto.jpeg',
        state='NCR',
        city='Noida',
    )
    return alexsanda


class User:

    def __init__(self, *, firstName, lastName, userEmail, userNumber, address, radio_button_type,
                 gender_value, date_type, month, year, day, input_subject, select_subject,
                 checkbox_type, checkbox_value, picture_name, state, city):
        self.firstName = firstName
        self.lastName = lastName
        self.userEmail = userEmail
        self.userNumber = userNumber
        self.address = address
        self.radio_button_type = radio_button_type
        self.gender_value = gender_value
        self.date_type = date_type
        self.month = month
        self.year = year
        self.day = day
        self.input_subject = input_subject
        self.select_subject = select_subject
        self.checkbox_type = checkbox_type
        self.checkbox_value = checkbox_value
        self.picture_name = picture_name
        self.state = state
        self.city = city

