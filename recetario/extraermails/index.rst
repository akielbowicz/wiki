.. title: Extraer direcciones de email de un texto


Código
::::::

.. code-block:: python

    >>> import re
    >>> mailsrch = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
    >>> mailsrch.findall(texto)


El código anterior devuelve una lista de strings, donde cada string es una dirección de email. El texto original puede contener basura como espacios, comas u otros caracteres.

Ahora podemos `atrapar al asesino`_ sin recurrir a Perl!!

La expresión regular que sigue es del proyecto django_.

.. code-block:: python

    email_re = re.compile(
                r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*"  # dot-atom
                r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-011\013\014\016-\177])*"' # quoted-string
                r')@(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?$', re.IGNORECASE)  # domain


Se puede utilizar en la receta de Juanjo arriba.

Autor
:::::

JuanjoConti_

Fuente
::::::

http://code.activestate.com/recipes/138889-extract-email-addresses-from-files/

.. ############################################################################

.. _atrapar al asesino: http://xkcd.com/208/

.. _django: http://code.djangoproject.com/browser/django/trunk/django/core/validators.py#L116

.. _juanjoconti: /juanjoconti
