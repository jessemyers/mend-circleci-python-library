from mend_circleci_python_library.generator import CircleCIGenerator


def test_generator() -> None:
    generator = CircleCIGenerator.from_parameters(
        project="foo",
        image="cimg/python:3.9.6",
    )

    tree = generator.generate()

    assert len(tree) == 1
    assert ".circleci/config.yml" in tree

    blob = tree[".circleci/config.yml"]
    data = blob.read().decode("utf-8")

    assert data is not None
