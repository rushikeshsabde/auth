"""empty message

Revision ID: a46a402e5f9a
Revises: c00084e36aae
Create Date: 2018-08-02 23:35:41.960898

"""

# revision identifiers, used by Alembic.
revision = 'a46a402e5f9a'
down_revision = 'c00084e36aae'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('resources', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('resources', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('groups', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
