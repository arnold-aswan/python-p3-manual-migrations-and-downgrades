"""renaming students_name column

Revision ID: f436519b2538
Revises: 791279dd0760
Create Date: 2023-08-31 12:56:57.788585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f436519b2538'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name = 'students_name')


def downgrade() -> None:
    op.alter_column('students', 'students_name', new_column_name = 'name')
