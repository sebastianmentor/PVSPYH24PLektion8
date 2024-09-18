def rita_rätvinklig_triangel(höjd):
    """Ritar ut en triangel i terminalen baserat på höjden 'höjd'."""
    
    if type(höjd) != int:
        print("Höjden på pyramiden måste vara ett heltal!")
        return
    
    for i in range(höjd-1):
        print('|'+ ' '*i + '\\')

    print('|' + '_'*(höjd-1) + '\\')


rita_rätvinklig_triangel(3)
rita_rätvinklig_triangel(5)
rita_rätvinklig_triangel(10)