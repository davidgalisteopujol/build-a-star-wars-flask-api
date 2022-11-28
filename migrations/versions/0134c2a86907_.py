"""empty message

Revision ID: 0134c2a86907
Revises: b415ed63d45a
Create Date: 2022-11-27 11:20:15.355676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0134c2a86907'
down_revision = 'b415ed63d45a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites_planets', schema=None) as batch_op:
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favorites_planets', schema=None) as batch_op:
        batch_op.alter_column('planet_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###