"""add content column to posts table

Revision ID: fd01694ca5ac
Revises: 4973b07d6188
Create Date: 2026-02-25 03:19:29.921036

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd01694ca5ac'
down_revision: Union[str, Sequence[str], None] = '4973b07d6188'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
