class Patient:
  #write a constructor
  def __init__(self, id, name, age, bloodgroup ):
    self.id = id
    self.name = name
    self.age = age
    self.bloodgroup = bloodgroup
    self.next = None
    self.prev = None


class WRM:

  def __init__(self):
    #Creating the dummy head
    self.dh = Patient(None,None,None,None)
    self.dh.next = self.dh
    self.dh.prev = self.dh

  def registerPatient(self,id, name, age, bloodgroup):
    #To Do
        current = self.dh.next
        while current != self.dh:
            if current.id == id:
                return "Unsuccessful! ID already taken."
            current = current.next
        new_patient = Patient(id, name, age, bloodgroup)

        new_patient.next = self.dh.next
        new_patient.prev = self.dh
        self.dh.next.prev = new_patient
        self.dh.next = new_patient
        return "Patient added successfully."



  def servePatient(self):
    #To Do
        if self.dh.next == self.dh:
            return "No patient left to serve."
        patient_to_serve = self.dh.next
        self.dh.next = patient_to_serve.next
        patient_to_serve.next.prev = self.dh
        return f'{patient_to_serve.name} served successfully.'


  def showAllPatient(self):
    #To Do
        if self.dh.next == self.dh: 
            print("No patients waiting.")
            return
        current = self.dh.next
        print("Patients in the waiting room:")
        while current != self.dh:
            print(f'ID: {current.id}, Name: {current.name}, Age: {current.age}, Blood Group: {current.bloodgroup}')
            current = current.next 

  def canDoctorGoHome(self):
    #To Do
    if self.dh.next == self.dh:
      return True
    else:
      return False
      
  def cancelAll(self):
    #To Do
        if self.dh.next == self.dh:
            print('\nNo appointment left to be cancelled.\n')
            return
        current = self.dh.next
        while current != self.dhd:
            t = current.next
            del current
            current = t
        self.dh.next = self.dh
        self.dh.prev = self.dh
        print('\nAll appointments are cancelled successfully. Doctor can go to lunch.\n')

  def ReverseTheLine(self):
    #To Do
        if self.dh.next == self.dh:
            return "No patients to reverse."
        current = self.dh.next 
        prev_patient = self.dh
        while current != self.dh:
            next_patient = current.next
            current.next = prev_patient
            current.prev = next_patient
            prev_patient = current
            current = next_patient
        self.dh.next.prev = self.dh
        self.dh.next = prev_patient
        return "Success"




print("**Welcome to Waiting Room Management System**")
print('\nChoose an option: (1,2,3... pick a number)\n')
print('1 - Register a patient.')
print('2 - Serve a patient.')
print('3 - Cancel all appointments')
print('4 - Check if doctor can go home')
print('5 - Show all patients.')
print('6 - To Exit.')


w = WRM()
while True:
    x = input("\nEnter your choice: \n")

    if not x.isdigit():
        print('\nInvalid option. Please enter a number between 1 and 6.\n')
        continue

    choice = int(x)

    if choice == 1:
        id = input('Enter ID: ')
        name = input('Enter Name: ')
        age = input('Enter Age: ')
        bloodgroup = input('Enter Blood Group: ')

        result = w.registerPatient(id, name, age, bloodgroup)
        print(result)

    elif choice == 2:
        result = w.servePatient()
        print(result)

    elif choice == 3:
        w.cancelAll()

    elif choice == 4:
      if w.canDoctorGoHome():
        print('Yes, the doctor can go home.')
      else:
        print('No, the doctor cannot go home.')

    elif choice == 5:
        w.showAllPatient()

    elif choice == 6:
        break

    else:
        print('\nInvalid option. Please enter a number between 1 and 6.\n')