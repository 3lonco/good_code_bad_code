# プレーヤーの攻撃力を合算する
def sumPlayerAttackPower(playerArmPower, playerWeaponPower):
    return playerArmPower + playerWeaponPower


# 敵の防御力を合算する
def sumEnemyDefence(enemyBodyDefence, enemyArmorDefence):
    return enemyBodyDefence + enemyArmorDefence


# ダメージ量を評価する
def estimateDamage(totalPlayerAttackPower, totalEnemyDefence):
    return totalPlayerAttackPower - totalEnemyDefence
