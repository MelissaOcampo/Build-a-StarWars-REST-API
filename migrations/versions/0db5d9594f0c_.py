"""empty message

Revision ID: 0db5d9594f0c
Revises: eeee87dc0d89
Create Date: 2023-01-26 17:30:33.296754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0db5d9594f0c'
down_revision = 'eeee87dc0d89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('created', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vehiculos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cargo_capacity', sa.String(length=250), nullable=True),
    sa.Column('consumables', sa.String(length=250), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vehiculos_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('planetas_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'planetas', ['planetas_id'], ['id'])
        batch_op.create_foreign_key(None, 'vehiculos', ['vehiculos_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('favoritos', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('planetas_id')
        batch_op.drop_column('vehiculos_id')

    op.drop_table('vehiculos')
    op.drop_table('planetas')
    # ### end Alembic commands ###