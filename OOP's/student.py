class Students:
    student_count = 0
    def __init__(self, name, email, age, phone, address, hobbies):
        self.age = age
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.hobbies = hobbies
        Students.student_count += 1
    
    def __str__(self):
        print("Student's name: " + self.name)
        print("Student's age: " + self.age)
        print("Student's E-mail: " + self.email)
        print("Student's phone number: " + self.phone)
        print("Student's residence: " + self.address)
        print("Student's interests: " + self.hobbies)
    

Student1 = Students("Michael", "Michael@gmail.com", 14, 9911515178, "90 Carson St.Huntersville, NC 28078", ["Dancing", "Reading", "Programming"])
Student2 = Students("Riley", "Riley@gmail.com", 15, 6127935437, "8528 Edgewood StreetSunnyside, NY 11104", ['Singing', 'Breadmaking', 'Cooking'])
Student3 = Students("Harley", "Harley@gmail.com", 12, 7887728980, "44 E. West Street Ashland, OH 44805", ['Astrology', 'Beatboxing', 'Cardistry'])
Student4 = Students("Osbert", "Osbert@gmail.com", 16, 7931373291, "131 Iroquois Street Southgate, MI 48195", ['Aquascaping', 'Singing', 'Breadmaking'])
Student5 = Students("Brian", "Brian@gmail.com", 13, 8161751587, "8779 Windsor St. Fuquay Varina, NC 27526", ['Drama', 'Beatboxing'])
Student6 = Students("Sophia", "Sophia@gmail.com", 17, 7129669461, "7075 Princess Street Linden, NJ 07036", ['Beatboxing', 'Community Activism'])
Student7 = Students("Peter", "Peter@gmail.com", 19, 6129528266, "7459 Gulf Lane Raeford, NC 28376", ['Aquascaping', 'Breadmaking', 'Singing'])
Student8 = Students("Celia", "Celia@gmail.com", 17, 8917622909, "9057 Vermont Road Cockeysville, MD 21030", ['Aquascaping', 'Drama'])
Student9 = Students("Nicholas", "Nicholas@gmail.com", 15, 6127985621, "7365 Cherry Hill Court Kingston, NY 12401", ['Astrology', 'Singing', 'Cooking'])
Student10 = Students("Harper", "Harper@gmail.com", 18, 6127967267, "8551 St Margarets Road Seymour, IN 47274", ['Singing', 'Breadmaking', 'Aquascaping'])
Student11 = Students("Jenson", "Jenson@gmail.com", 18, 6127975879, "318 Lydall Street, Manchester CT 06042", ['Singing', 'Astrology', 'Beatboxing'])
Student12 = Students("Betty", "Betty@gmail.com", 20, 6127990571, "1330 West 82nd Avenue, Anchorage AK 99518", ['Community Activism', 'Beatboxing', 'Aquascaping'])
Student13 = Students("Angela", "Angela@gmail.com", 14, 6127956553, "4920 Quonset Drive, Sacramento CA 95820", ['Drama', 'Breadmaking', 'Beatboxing'])
Student14 = Students("Frederik", "Frederik@gmail.com", 16, 8847386584, "8772 West 79th Avenue, Arvada CO 80005", ['Breadmaking', 'Aquascaping'])
Student15 = Students("Bittu", "Bittu@gmail.com", 15, 9672432854, "2703 Woolsey Street, Berkeley CA 94705", ["Dancing", "Reading", "Programming"])
Student16 = Students("Anthony", "Anthony@gmail.com", 13, 6734053058, "595 West 54th Street, Savannah GA 31405", ['Beatboxing', 'Drama', 'Community Activism'])
Student17 = Students("Salena", "Salena@gmail.com", 13, 7538634920, "5205 West Thunderbird Road, Glendale AZ 85306", ['Cardistry', 'Beatboxing', 'Drama'])
Student18 = Students("Bruno", "Bruno@gmail.com", 12, 5584257208, "6431 Shattuck Avenue, Oakland CA 94609", ['Breadmaking', 'Aquascaping', 'Beatboxing'])
Student19 = Students("Zachary", "Zachary@gmail.com", 14, 8423571634, "2686 Avery Park Drive, Nashville TN 37211", ['Beatboxing', 'Drama', 'Singing'])
Student20 = Students("Harry", "Harry@gmail.com", 20, 5589377143, "1255 U.S. Route 5 North, Windsor VT 05089", ['Cooking', 'Singing', 'Breadmaking'])