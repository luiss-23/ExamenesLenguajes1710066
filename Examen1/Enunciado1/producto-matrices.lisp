;;; Programa en el que se implementara el producto de matrices

(defun producto-matrices (a b)
    "Funcion que calculara el producto de dos matrices a y b de dimensiones
    NxM y MxP respecticvamente, resutlando del producto una matriz de dimensiones
    NxP"
    (setq dimensiones-m1 (array-dimensions a))
    (setq dimensiones-m2 (array-dimensions b))
    (setq c (make-array (list (nth 0 dimensiones-m1) (nth 1 dimensiones-m2))))
    (dotimes (i (nth 0 dimensiones-m1))
        (dotimes (j (nth 1 dimensiones-m2))
            (setf (aref c i j) 0)
            (dotimes (k (nth 0 dimensiones-m2))
                (setf (aref c i j) (+ (aref c i j) (* (aref a i k) (aref b k j))))
            )
        )
    )

    (return-from producto-matrices c)
)

;;; main()
(format t "Ingrese el valor de N: ")
(defvar N (read))
(format t "Ingrese el valor de M: ")
(defvar M (read))
(format t "Ingrese el valor de P: ")
(defvar P (read))

(setq mat1 (make-array (list N M)))
(format t "Ingresar datos de la matriz 1~%")
(dotimes (i N)
    (dotimes (j M)
        (format t "Ingrese el elemento de la casilla [~d, ~d]: " i j)
        (setf (aref mat1 i j) (read))
    )
)
(setq mat2 (make-array (list M P)))
(format t "Ingresar datos de la matriz 2~%")
(dotimes (i M)
    (dotimes (j P)
        (format t "Ingrese el elemento de la casilla [~d, ~d]: " i j)
        (setf (aref mat2 i j) (read))
    )
)

(defvar matriz-resultado (producto-matrices mat1 mat2))
(dotimes (i N)
    (format t "[")
    (dotimes (j P)
        (format t " ~d" (aref matriz-resultado i j))
    )
    (format t "]~%")
)