from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.db.models import Exam, Student
from app.modules.students.models import OnboardingStatus


def test_student_can_select_multiple_exams():
    engine = create_engine(
        "postgresql+psycopg://postgres@localhost:5450/mpsc_engine"
    )

    with Session(engine) as session:
        student = Student(
            telegram_user_id=999999999,
            onboarding_status=OnboardingStatus.PENDING,
        )

        group_b = session.query(Exam).filter_by(code="GROUP_B").one()
        group_c = session.query(Exam).filter_by(code="GROUP_C").one()

        student.exams.extend([group_b, group_c])

        session.add(student)
        session.commit()

        session.refresh(student)

        assert {exam.code for exam in student.exams} == {
            "GROUP_B",
            "GROUP_C",
        }

        session.delete(student)
        session.commit()