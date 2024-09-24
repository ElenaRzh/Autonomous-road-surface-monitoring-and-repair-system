
![обложка1](https://github.com/user-attachments/assets/93c8e315-d91e-4076-980b-6bba40b66471)


## Проблема и цель
Создание системы, которая позволит осуществлять мониторинг состояния дорожного полотна с помощью квадрокоптера и проводить ремонт обнаруженных дефектов автономным ровером.
## Описание работы
Квадрокоптер автономно выполняет облет городских улиц и при помощи нейронной сети обнаруживает ямы и дефекты дорожного полотна. Все данные о найденных дефектах отправляются на сервер, который составляет карту повреждений. По ночам, когда автомобилей на дорогах меньше, автономный ровер выезжает на ремонт дороги. Он передвигается по заранее составленному маршруту, соблюдая ПДД, распознавая показания светофоров и прочее. По прибытии на место работ ровер при помощи лидара сканирует яму, определяет ее размер и объем. На основе полученных данных он принимает решение о самостоятельном ремонте либо же передаче информации о том, что эту яму необходимо устранять вручную. Если яма пригодна для автономного ремонта, он подает необходимый объем асфальтобетонной смеси в яму, а затем проезжается по ней, выравнивая ее.
## Задачи проекта
- Подготовить датасет и обучить нейронную сеть на распознавание ям тестовой карты.
- Настроить дрон под работу в автономном режиме. Загрузить и отладить работу нейронной сети на дроне.
- Разработать алгоритм работы с результатами распознавания: подсчет количества ям, определение их координат, передача данных на сервер.
- Разработать серверное приложение с функцией приема данных с дрона, обработке данных о ямах, сборе статистики и передаче информации об обнаруженных ямах пользователям.
- Протестировать систему и внести изменения на основе результатов тестирования.

## **Команда проекта**


| Участник | Роль | Задача |
|----------|------|--------|
| Шерстобитов Олег Андреевич | Программист | Программирование дрона |
| Ржанникова Елена Андреевна | Программист | Работа с ИИ |


[Реализация проекта](https://github.com/ElenaRzh/Autonomous-road-surface-monitoring-and-repair-system./blob/main/DEVELOPMENT.md)


