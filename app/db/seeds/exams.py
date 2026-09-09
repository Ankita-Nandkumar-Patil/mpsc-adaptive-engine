from sqlalchemy import select

from app.db.session import SessionLocal
from app.modules.exams.models import Exam


EXAMS = [
    {
        "name": "MPSC Group B",
        "code": "GROUP_B",
    },
    {
        "name": "MPSC Group C",
        "code": "GROUP_C",
    },
]


def seed_exams() -> None:
    with SessionLocal() as session:
        for exam_data in EXAMS:
            existing_exam = session.scalar(
                select(Exam).where(Exam.code == exam_data["code"])
            )

            if existing_exam is None:
                session.add(Exam(**exam_data))

        session.commit()


if __name__ == "__main__":
    seed_exams()