"""modelspy img

Revision ID: ca070217836a
Revises: f5741d57c43f
Create Date: 2023-04-19 10:28:04.180237

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca070217836a'
down_revision = 'f5741d57c43f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.add_column(sa.Column('img', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.drop_column('img')

    # ### end Alembic commands ###
