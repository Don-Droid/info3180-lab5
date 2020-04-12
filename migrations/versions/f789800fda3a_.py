"""empty message

Revision ID: f789800fda3a
Revises: fc3e4c6c300f
Create Date: 2020-03-11 23:53:10.161694

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f789800fda3a'
down_revision = 'fc3e4c6c300f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('profiles', sa.Column('photo', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('profiles', 'photo')
    # ### end Alembic commands ###
