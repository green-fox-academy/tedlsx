import random

class patient:
    def __init__(self, severity = 0):
        self.severity = severity

    def retrieve(self):
        self.severity = random.randint(0, 10)

    def treat(self):
        self.severity -= 1


class queue(patient):
    def __init__(self, patient_list):
        patient.__init__(self)
        self.severity = severity
        self.patient_list = patient_list
    def add(self, severity):
        p = patient(severity)
        self.patient_list.append(p)

class hospital(queue):
    def __init__(self, patient_list):
        queue.__init__(self, patient_list)
        self.patient_list = patient_list


class safequeue:
    def __init__(self, queue):
        queue.__init__(self, patient_list)
        self.patient_list = patient_list

    def find(self):
        highest_severity = 0
        for patient in self.patient_list:
            self.patient_list = [i if i.severity > 0 for i in self.patient_list]
            if highest_severity <= patient.severity:
                highest_severity = patient.severity
            elif len(self.patient_list) = 0:
                return "null"
        return patient

class classicqueue():
    def __init__(self, queue):
        queue.__init__(self, patient_list)
        self.patient_list = patient_list
        self.patient_list = self.patient_list[1:] + [self.patient_list[0]]
        for patient in self.patient_list:
            if patient.severity != 0:
                return patient
            elif len(self.patient_list) == 0:
                return  "null"