from sqlalchemy import create_engine, asc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

today = datetime.today()
Base = declarative_base()


def user_menu():
    print("1) Today's tasks")
    print("2) Week's tasks")
    print("3) All tasks")
    print("4) Missed tasks")
    print("5) Add task")
    print("6) Delete task")
    print("0) Exit")
    user_input = input()
    return user_input


engine = create_engine('sqlite:///todo.db?check_same_thread=False')


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def today_(selected_date=None):
    if selected_date is not None:
        print(f"{selected_date.strftime('%A')} {selected_date.day} {selected_date.strftime('%b')}:")
    else:
        print(f"Today {today.day} {today.strftime('%b')}:")


def select_today_task():
    rows = session.query(Table).filter(Table.deadline == today.date()).all()
    if len(rows) == 0:
        print()
        today_()
        print("Nothing to do!")
    else:
        print()
        today_()
        counter = 1
        for i in rows:
            print(str(counter) + ".", i.task)
            counter += 1
        print()


def select_weeks_tasks():
    for i in range(7):
        selected_date = today + timedelta(i)
        rows = session.query(Table).filter(Table.deadline == selected_date.date()).all()
        if len(rows) == 0:
            print()
            today_(selected_date)
            print("Nothing to do!")
        else:
            print()
            today_(selected_date)
            counter = 1
            for a in rows:
                print(str(counter) + ".", a.task)
                counter += 1
    print()



def select_all_task():
    rows = session.query(Table).order_by(asc(Table.deadline)).all()
    if len(rows) == 0:
        print()
        print("All tasks:")
        print("Nothing to do!")
    else:
        print()
        print("All tasks:")
        counter = 1
        for i in rows:
            date_string = i.deadline
            date_ = datetime.strftime(date_string, "%d %b").lstrip("0").replace(" 0", " ")
            print(f"{str(counter)}. {i.task}. {date_}")
            counter += 1
        print()


def select_missed_tasks():
    rows = session.query(Table).filter(Table.deadline < today.date()).order_by(asc(Table.deadline)).all()
    if len(rows) == 0:
        print()
        print("Missed tasks:")
        print("Nothing is missed!")
        print()
    else:
        print()
        print("Missed tasks:")
        counter = 1
        for i in rows:
            date_string = i.deadline
            date_ = datetime.strftime(date_string, "%d %b").lstrip("0").replace(" 0", " ")
            print(f"{str(counter)}. {i.task}. {date_}")
            counter += 1
        print()


def delete_task():
    rows = session.query(Table).filter(Table.deadline <= today.date()).order_by(asc(Table.deadline)).all()
    if len(rows) == 0:
        print()
        print("Nothing to delete!")
        print()

    else:
        print()
        print("Choose the number of the task you want to delete:")
        counter = 1
        for i in rows:
            date_string = i.deadline
            date_ = datetime.strftime(date_string, "%d %b").lstrip("0").replace(" 0", " ")
            print(f"{str(counter)}. {i.task}. {date_}")
            counter += 1
        task_to_delete = int(input()) - 1
        session.delete(rows[task_to_delete])
        print("The task has been deleted!")
        print()
    session.commit()


def add_task():
    print("Enter task")
    task_input = input()
    print("Enter deadline")
    deadline_input = input()
    date_ = datetime.strptime(deadline_input, '%Y-%m-%d')
    new_task = Table(task=f'{task_input}', deadline=datetime.date(date_))
    session.add(new_task)
    session.commit()
    print("The task has been added!")
    print()


def start():
    while True:
        user_input = user_menu()
        if user_input == '0':
            print("Bye!")
            exit()
        elif user_input == '1':
            select_today_task()
        elif user_input == '2':
            select_weeks_tasks()
        elif user_input == '3':
            select_all_task()
        elif user_input == '4':
            select_missed_tasks()
        elif user_input == '5':
            add_task()
        elif user_input == '6':
            delete_task()


start()
