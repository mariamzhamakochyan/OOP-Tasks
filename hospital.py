class Patient:
    def __init__(self, id, name, hospital_room):
        self.id = id
        self.name = name
        self.hospital_room = hospital_room
    
class Hospital:
    def __init__(self, name, patient_number):
        self.name = name
        self.patient_number = patient_number
        self.patients = []
    
    def add(self, patient):
        if len(self.patients) >= self.patient_number:
            print("The hospital is full!")
        else:
            patient_dictionary = {
            'ID': patient.id,
            'Name': patient.name,
            'Hospital Room': patient.hospital_room
            }
            self.patients.append(patient_dictionary)
            print( '{} has been admitted.'.format(patient.name))
            
            
    def discharge(self, name):
        for value in self.patients:
            if value['Name'] == name:
                value['Hospital Room'] = None
                self.patients.remove(value)
               
patient1 = Patient(1, 'Dan',  142)
patient2 = Patient(2, 'Maks', 324)
patient3 = Patient(3, 'Nicky', 158)
patient4 = Patient(4, 'Roger', 253)
patient5 = Patient(5, 'Maluma', 123)


hospital = Hospital('Hospital', 4)
hospital.add(patient1)
hospital.add(patient2)
hospital.add(patient3)
hospital.add(patient4)
hospital.add(patient5)
hospital.discharge('Maluma')
hospital.discharge('Roger')
