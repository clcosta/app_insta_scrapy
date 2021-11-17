class PrivateProfileError(Exception):
    """
    Error para perfil privado no instagram.
    """

    def __str__(self):
        return "Perfil Privado Error"

    def __name__(self):
        return "Perfil Privado Error"

    def __init__(
        self,
        message="O perfil deste usuario no instagram é privado!",
        user=None,
    ):
        self.user = user
        super().__init__(message)
