"""empty message

Revision ID: 52b001b6421b
Revises: d18e57daa4e2
Create Date: 2022-11-25 17:49:38.513542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52b001b6421b'
down_revision = 'd18e57daa4e2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('diameter',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planet', schema=None) as batch_op:
        batch_op.alter_column('diameter',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('description',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)

    # ### end Alembic commands ###
