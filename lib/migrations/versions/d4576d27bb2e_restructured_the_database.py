"""restructured the database

Revision ID: d4576d27bb2e
Revises: 940f7c1d29b1
Create Date: 2024-09-27 16:58:03.753795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4576d27bb2e'
down_revision: Union[str, None] = '940f7c1d29b1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
