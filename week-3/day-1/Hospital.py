import random

class patient:
    def __init__(self, severity = 0):
        self.severity = severity
        self.severity = random.randint(0, 10)

    def retrieve(self):
        return self.severity

    def treat(self):
        self.severity -= 1

class queue():
    def __init__(self, patient_list):
        self.patient_list = patient_list
    def add(self, severity):
        p = patient(severity)
        self.patient_list.append(p)
    def get_next(self):
        self.patient_list.pop([0])

class hospital():
    def __init__(self, patient_list):
        self.patient_list = patient_list
        self.queue = safequeue(self.patient_list)

    def treat_next_patient():
        self.queue.get_next().treat()


class safequeue(queue):
    def __init__(self, queue):
        queue.__init__(self, patient_list)

    def get_next(self):
        patient_severity_list = []
        for self.patient in self.patient_list:
            self.patient_list = list(filter(lambda x: x.retrieve() > 0, self.patient_list))
            patient_severity_list.append(self.patient.severity)
        self.patient_list.insert(0, max(patient_severity_list))
        self.patient_list.remove(max(patient_severity_list))
        if len(self.patient_list) == 0:
            return None
        for patient in self.patient_list:
            if patient.severity == max(patient_severity_list):
                return patient 

class classicqueue(queue):
    def __init__(self, queue):
        queue.__init__(self, patient_list)

    def get_next(self):
        for patient in self.patient_list:
            if patient.severity == 0:
                self.patient_list.remove(patient)
        if len(self.patient_list) == 0:
            return  None
        self.patient_list = self.patient_list[1:] + self.patient_list[0]
        return self.patient_list[-1]

a = patient()
b = patient()
qu = queue([a, b])
print(a.severity)
print(b.retrieve())
print(b.retrieve())
print(qu)
hos = hospital([a, b])