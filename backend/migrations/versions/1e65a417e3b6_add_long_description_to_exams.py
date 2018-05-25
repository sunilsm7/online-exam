"""add long_description to exams

Revision ID: 1e65a417e3b6
Revises: 
Create Date: 2018-05-25 17:04:49.237312

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e65a417e3b6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('exams', sa.Column(
        'long_description',
        sa.Text,
        nullable=False,
        server_default='Default exam description'))


def downgrade():
    pass
