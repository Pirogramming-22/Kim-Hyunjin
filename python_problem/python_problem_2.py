import re

#함수 이름은 변경 가능합니다.
class Student:
    def __init__(self, name, mid_score, final_score):
        self.name = name
        self.mid_score = mid_score
        self.final_score = final_score
        self.grade = None
        #self.grade = Student.determineGrade(mid_score, final_score)
    
    @classmethod
    def createNewStudent(cls, name, mid_score, final_score):
        return cls(name, int(mid_score), int(final_score))
    
    def getName(self):
        return self.name
    
    def getMid(self):
        return self.mid_score
    
    def getFinal(self):
        return self.final_score
    
    def getGrade(self):
        return self.grade
    
    def setGrade(self, grade):
        self.grade = grade
        
#menu1에서 활용할 exception
class programError(Exception):
    def __init__(self, error_message):
        super().__init__(error_message)

def update_check(input_history):
    for k,v in input_history.items():
        if not v:
            return False
    return True
##############  menu 1
def Menu1(inputs, input_history) :
    #사전에 학생 정보 저장하는 코딩 
    input_history[inputs[0]] = False
    st = Student.createNewStudent(inputs[0], inputs[1], inputs[2])
    data.append(st)
##############  menu 2
def Menu2(data, input_history) :
    #학점 부여 하는 코딩
    print("Grading to all students.")
    for st in data:
        if not input_history[st.getName()]:
            average_score = (st.getMid()+st.getFinal())/2
            if average_score >= 90:
                st.setGrade('A')
            elif average_score >= 80:
                st.setGrade('B')
            elif average_score >= 70:
                st.setGrade('C')
            else:
                st.setGrade('D')
            input_history[st.getName()] = True
##############  menu 3
def Menu3(data) :
    #출력 코딩
    print("------------------------------------")
    print("name\tmid\tfinal\tgrade")
    for st in data:
        print(f'{st.getName()}\t{st.getMid()}\t{st.getFinal()}\t{st.getGrade()}')
    print("------------------------------------")
##############  menu 4
def Menu4(inputs, data, input_history):
    del(input_history[inputs])
    for i in range(len(data)):
        if data[i].getName() == inputs:
            data.remove(data[i]);
            print(f'{inputs} student information is deleted')
            return
#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
data = []
input_history ={}
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출
        pattern = r"^[1-9]\d*$" #양의 정수 정규식
        error_message1="Num of data is not 3!" 
        error_message2="Score is not positive integer!"
        error_message3="Already exist name!"
        
        inputs = input("Enter name mid-score final-score: ").split(" ")
        
        try:
            if len(inputs)==3 and re.fullmatch(pattern, inputs[1]) and re.fullmatch(pattern, inputs[2]) and inputs[0] not in input_history:
                Menu1(inputs, input_history)
            elif len(inputs)!=3:
                raise programError(error_message1)
            elif not re.fullmatch(pattern, inputs[1]) or  not re.fullmatch(pattern, inputs[2]):
                raise programError(error_message2)
            elif inputs[0] in input_history:
                raise programError(error_message3)
        except programError as e:
            print(e)
            
    elif choice == "2" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력
        error_message="No student data!"
        try:
            if len(data)>0:
                Menu2(data, input_history)
            else:
                raise programError(error_message)
        except programError as e:
            print(e)

    elif choice == "3" :
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출
        error_message1="No student data!" 
        error_message2="There is a student who didn't get grade."
        try:
            if len(data)>0 and update_check(input_history):
                Menu3(data)
            elif len(data) == 0:
                raise programError(error_message1)
            elif not update_check(input_history):
                raise programError(error_message2)
        except programError as e:
            print(e)

    elif choice == "4" :
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력
        error_message1="No student data!"
        error_message2="Not exist name!"
        error_message3="Wrong input!"
        try:
            if len(data) == 0:
                raise programError(error_message1)
            inputs = input("Enter the name to delete: ")
            if inputs in input_history:
                Menu4(inputs, data, input_history)
            elif inputs not in input_history:
                raise programError(error_message2)
            else:
                raise programError(error_message3)
        except programError as e:
            print(e)

    elif choice == "5" :
        #프로그램 종료 메세지 출력
        #반복문 종료
        print("Exit Program!")
        break

    else :
        #"Wrong number. Choose again." 출력
        error_message="Wrong number. Choose again."
        print(error_message)